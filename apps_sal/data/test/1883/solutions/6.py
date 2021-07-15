import sys

def solve():
    n = int(input())
    types = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = list()
    count = [0] * (n + 1)
    for val in a:
        count[val-1]+=1
    for i in range(n):
        if types[i] == 1:
            temp = list()
            cur = i
            while True:
                if count[cur] > 1 or cur < 0: break
                temp.append(cur + 1)
                cur = a[cur] - 1
            if len(temp) > len(res):
                res = temp
    print(len(res))
    return ' '.join(map(str, res[::-1]))

if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
print(solve())
