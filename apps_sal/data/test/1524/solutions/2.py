def main():
    s = input()
    ans = [0]*len(s)
    pos = [-1]*len(s)
    x = None
    for i in range(len(s)):
        if s[i] == "L":
            if x is None:
                x = i
            pos[i] = x
        else:
            x = None
    x = None
    for i in reversed(range(len(s))):
        if s[i] == "R":
            if x is None:
                x = i
            pos[i] = x
        else:
            x = None
    for i in range(len(s)):
        dist = abs(pos[i] - i)
        if dist % 2 == 0:
            ans[pos[i]] += 1
        else:
            if s[i] == "L":
                ans[pos[i]-1] += 1
            else:
                ans[pos[i]+1] += 1
    for v in ans:
        print(v, end=" ")

def __starting_point():
    main()
__starting_point()
