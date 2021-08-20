import sys
input = sys.stdin.readline


def r1():
    return int(input())


def r2():
    return list(map(int, input().split()))


pred = {}
size = {}
k = 0


def get_lead(index):
    if pred[index] == index:
        return index
    pred[index] = get_lead(pred[index])
    return pred[index]


def merge(a, b, k):
    pred_a = get_lead(a)
    pred_b = get_lead(b)
    if pred_a == pred_b:
        return k
    k -= 1
    if size[pred_a] > size[pred_b]:
        (pred_a, pred_b) = (pred_b, pred_a)
    pred[pred_a] = pred_b
    size[pred_b] = max(size[pred_b], size[pred_a] + 1)
    return k


n = r1()
for i in range(n):
    psw = input()
    first = psw[0]
    for item in psw:
        if item == '\n':
            break
        if item not in pred:
            pred[item] = item
            size[item] = 1
            k += 1
        k = merge(item, first, k)
print(k)
