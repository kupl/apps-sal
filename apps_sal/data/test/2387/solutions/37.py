def count_scan(s):
    max_min = 0
    compare = 0
    for c in s:
        if c == '(':
            compare += 1
        elif c == ')':
            compare -= 1
            max_min = min(max_min, compare)
    return min(max_min, compare), compare
 
 
def key(lst):
    m, c = lst
    if c > 0:
        return 1, m
    else:
        return -1, c - m
 
 
def main():
    n = int(input())
    lst = [input() for _ in range(n)]
 
    txt = 'No'
    ans = 0
    for max_min, c in sorted([count_scan(s) for s in lst],
                             reverse=True,
                             key=key):
        if max_min + ans < 0:
            break
        ans += c
    else:
        if ans == 0:
            txt = 'Yes'
 
    print(txt)
  
def __starting_point():
    main()


__starting_point()
