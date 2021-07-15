# ABC126
# A Changing a Character
n, k = list(map(int, input().split()))
S = list(input())
x = S.pop(k-1).lower()
S.insert((k-1),x)
print(("".join(S)))

