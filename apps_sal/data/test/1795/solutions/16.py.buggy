# This code sucks, you know it and I know it.
# Move on and call me an idiot later.

n = int(input())

l = list(map(int, input().split()))

for i in l:
    a = i
    b = l[a - 1]
    c = l[b - 1]
    if a == l[c - 1] and a != b and b != c and c != a:
        print("YES")
        return
print("NO")
