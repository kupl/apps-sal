import itertools
 
 
def main():
    n = input()
    print(sev(n))
 
 
def sev(n: str) -> int:
    ret = 0
    d = len(n)
    while d > 2:
        for comb in itertools.product(['3', '5', '7'], repeat=d):
            s = ''.join(comb)
            if '3' in comb and '5' in comb and '7' in comb and int(s) <= int(n):
                ret += 1
        d -= 1
    return ret
 
 
def __starting_point():
    main()
__starting_point()
