def gc(a):
    ans = dict()
    for d in a:
        if d in list(ans.keys()):
            ans[d] += 1
        else:
            ans[d] = 1
    return ans[max(ans, key=lambda i: ans[i])]


def f(t, n, s):
    if t == s and n == 1:
        return s - 1
    return min(t + n, s)


n = int(input())
a = input()
b = input()
c = input()
size = len(c)
arr = [f(gc(a), n, size), f(gc(b), n, size), f(gc(c), n, size)]
if arr[0] > arr[1] and arr[0] > arr[2]:
    print('Kuro')
elif arr[1] > arr[0] and arr[1] > arr[2]:
    print('Shiro')
elif arr[2] > arr[1] and arr[2] > arr[0]:
    print('Katie')
else:
    print('Draw')
