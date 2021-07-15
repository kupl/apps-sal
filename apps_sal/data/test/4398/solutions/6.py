N = int(input())
S, T = map(str, input().split())

for s, t in zip(list(S), list(T)):
    print(s + t, end="")

print("")
