
__author__ = 'artyom'


def main():
    s = read(0)
    n = len(s)
    ex = 2 * s.count('(') - n
    if ex < 0:
        return -1
    res = []
    l = i = 0
    last = s.rfind('
    for i in range(n):
        c=s[i]
        if c == '(':
            l += 1
        elif c == ')':
            l -= 1
        else:
            if l == 0:
                return -1
            k=1 if i < last else 1 + ex
            res.append(k)
            l -= k
        if l < 0:
            return -1
    return res



def read(mode=1, size=None):
    if mode == 0:
        return input().strip()
    if mode == 1:
        return int(input().strip())
    if mode == 2:
        return input().strip().split()
    if mode == 3:
        return list(map(int, input().strip().split()))
    a=[]
    for _ in range(size):
        a.append(read(3))
    return a


def write(s="\n"):
    if s is None:
        s=''
    if isinstance(s, tuple) or isinstance(s, list):
        s='\n'.join(map(str, s))
    s=str(s)
    print(s, end="\n")


write(main())
