n = int(input())
# don't hack me lel or u can't hack me lol
l = list(map(int, input().split()))
l.sort()
if(n % 2 != 0):
    print(l[n // 2])
else:
    print(l[n // 2 - 1])
