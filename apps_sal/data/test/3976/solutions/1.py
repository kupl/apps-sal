from collections import Counter

n, m, p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def try_from(start, a, b):
    result = []
    seq = a[start::p]
    i = 0
    if len(seq) < len(b):
        return []

    counts_a = Counter(seq[:len(b)])
    counts_b = Counter(b)
    if counts_a == counts_b:
        result.append(start)

    for i in range(1, len(seq) - len(b) + 1):
        counts_a[seq[i-1]] -= 1
        counts_a[seq[i+len(b) - 1]] += 1
        if not counts_a[seq[i-1]]:
            del counts_a[seq[i-1]]

        ok = counts_a == counts_b
        #ok = sorted(seq[i:i+len(b)]) == sorted(b)

        if ok:
            result.append(start + p * i)

    return [x + 1 for x in result]


result = []
for start in range(p):
    result += try_from(start, a, b)

print(len(result))
print(' '.join(map(str, sorted(result))))





# Made By Mostafa_Khaled

