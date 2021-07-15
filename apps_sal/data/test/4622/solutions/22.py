n = int(input())
a = list(map(int,input().split()))
aa = set(a)
print("YES" if len(a) ==len(aa) else "NO")
