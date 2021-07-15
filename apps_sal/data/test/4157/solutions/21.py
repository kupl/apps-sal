def p3(n):
    res = 0
    while n % 3 == 0:
        n //= 3
        res += 1
    return res
def p2(n):
    res = 0
    while n % 2 == 0:
        n //= 2
        res += 1
    return res
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
def comp(x, y):
    return (p2(x) - p3(x)) - (p2(y) - p3(y))
n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr, key=cmp_to_key(comp))
s = str(arr[0])
for c in arr[1:]:
    s += f" {c}"
print(s)
