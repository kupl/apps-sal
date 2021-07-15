N = int(input())
S = list(input().split())

cnt = len(set(S))
print("Three" if cnt == 3 else "Four")
