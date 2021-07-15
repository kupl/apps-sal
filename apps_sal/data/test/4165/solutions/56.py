N = int(input())
L = sorted(list(map(int, input().split())))
print("Yes" if L[-1] < sum(L)-L[-1] else "No")
