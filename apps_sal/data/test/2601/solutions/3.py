# In the long run, we only hit what we aim at. Henry David Thoreau
# by : Blue Edge - Create some chaos

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a == sorted(a)[::-1] and len(set(a)) == n:
        print("NO")
    else:
        print("YES")
