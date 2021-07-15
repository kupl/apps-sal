n,a,b = map(int,input().split())
h_list = []
for _ in range(n):
    h = int(input())
    h_list.append(h)

def ba(s):
    count = 0
    for i in h_list:
        i -= s*b
        if i > 0:
            count += -(-i//(a-b))
    if count <= s:
        return True
    else:
        return False


ng = 0
ok = 10**9
while ok  > ng +1 :
    mid = (ng+ok)//2
    if ba(mid):
        ok = mid
    else:
        ng = mid

print(ok)
