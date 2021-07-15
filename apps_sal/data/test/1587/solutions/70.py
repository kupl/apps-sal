def solve1(n: int, c: str) -> int:
    ans = 0
    r, w = 0, 0
 
    for i in range(n):
        if c[i] == "R":
            r += 1
        else:
            w += 1
 
    s_pivot = c[:r] + "|" + c[r:]
    s_check = " " * r + "|"
 
    for i in range(r, n):
        if c[i] == "R":
            ans += 1
            s_check += "X"
        else:
            s_check += " "
 
    #print(s_pivot, s_check, sep="\n")
    return ans
 
 
n = int(input())
c = input()
 
print(solve1(n, c))
