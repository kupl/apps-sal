def run_length_compress(string):
    string = string + ["."]
    n = len(string)

    begin = 0
    end = 1
    cnt = 1
    ans = [] 
    while True: 
        if end >= n:
            break
        if string[begin] == string[end]:
            end += 1
            cnt += 1
        else:
            ans.append(string[begin])
            begin = end 
            end = begin + 1
            cnt = 1

    return ans


def lps(string): 
    n = len(string)
    dp = [[0]*n for _ in range(n)] 

    for i in range(n): 
        dp[i][i] = 1
  
    for cl in range(2, n+1): 
        for i in range(n-cl+1): 
            j = i + cl - 1
            
            if string[i] == string[j] and cl == 2: 
                dp[i][j] = 2
            elif string[i] == string[j]: 
                dp[i][j] = dp[i+1][j-1] + 2
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
  
    return dp[0][n-1]

n = int(input())
a = list(map(int, input().split()))

a = run_length_compress(a)
len_pal = lps(a)
print(len(a) - 1 - len_pal//2)

