def main():
    n = int(input())
    s = input()
    # 条件1:全パターンはr*g*b
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    # i, j, kの差が一致するもので条件1を満たすものを後から引く 
    cnt = 0
    # len(s)
    for i in range(n):
        for j in range(i+1, n):
                k = j + j - i
                if k >= n:
                    break
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    cnt += 1
    ans = r*g*b - cnt
    print(ans)
    
def __starting_point():
    main()
__starting_point()
