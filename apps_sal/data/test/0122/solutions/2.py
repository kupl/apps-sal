def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))


n = it()
a = lt()
k = 0
left = 0
right = sum(a)
bl = False
dict = {}
for i in range(n):
    if a[i] in dict:
        (ma, mi) = dict[a[i]]
        dict[a[i]] = (max(ma, i), min(mi, i))
    else:
        dict[a[i]] = (i, i)
while k < n and not bl:
    if right == left:
        bl = True
    elif right > left:
        x = (right - left) / 2
        if x == int(x) and int(x) in dict and dict[int(x)][0] >= k:
            bl = True
        else:
            right -= a[k]
            left += a[k]
            k += 1
    else:
        x = (left - right) / 2
        if x == int(x) and int(x) in dict and dict[int(x)][1] <= k - 1:
            bl = True
        else:
            right -= a[k]
            left += a[k]
            k += 1
if bl:
    pt("YES")
else:
    pt("NO")
