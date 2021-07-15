from sys import stdin, stdout

def rsingle_int():
    return int(stdin.readline().rstrip())

def rmult_int():
    return [ int(x) for x in stdin.readline().rstrip().split() ]

def r_str():
    return stdin.readline().rstrip()
    
def rsingle_char():
    return stdin.read(1)

data = {}

def foo(s, s_len, l, r):
   # print("{}:{}".format(l,r))
    diff = r - l
    if diff == 0:
        return (0, 0)
    if l not in data:
        data[l] = {}
    if r in data[l]:
        return data[l][r]
    else:
        res = None
        
        cookies = 0
        if diff == 1:
            left = s[l]
            right = s[r]
        else:
            cookies_1, left = foo(s, s_len, l, int(l + (diff / 2)))
            cookies_2, right = foo(s, s_len, int(l + (diff / 2) + 1), r)
            cookies += cookies_1 + cookies_2
        cookies += int((left + right) / 10)
        rem = int((left + right) % 10)
        data[l][r] = (cookies, rem)
        return (cookies, rem)
            

def main():
    s_len = rsingle_int()
    s = rmult_int()
    r_len = rsingle_int()
    for i in range(r_len):
        l, r = rmult_int()
        cookies, rem = foo(s, s_len, l - 1, r - 1)
        print(cookies)

 
main()
