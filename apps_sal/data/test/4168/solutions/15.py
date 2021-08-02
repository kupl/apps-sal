import itertools
N = int(input())

if N == 0:
    print(0)
    return
ans = []
while N != 0:
    ans.append(N % 2)
    N = -(N - N % 2) // 2
ans.reverse()
print("".join(list(map(str, ans))))
