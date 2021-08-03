def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))


n, m = mi()
s = input()

s = s[::-1]

ans = []
ima = 0
while ima != n:
    flag = False
    for i in range(m):
        tmp = m - i
        if ima + tmp > n:
            continue
        elif s[ima + tmp] == str(1):
            continue
        else:
            ima += tmp
            ans.append(tmp)
            flag = True
            break
    if flag == False:
        print((-1))
        return

print((*ans[::-1]))
