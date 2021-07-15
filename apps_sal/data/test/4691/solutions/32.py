def main():
    n = int(input())
    
    s = [input().rstrip('\r') for i in range(n)]
    li = ["AC", "WA", "TLE", "RE"]
    cnt = 0
    
    for i in range(len(li)):
        for j in s:
            if li[i] == j:
                cnt += 1
        print(li[i] + " x " + str(cnt))
        cnt = 0
    
    
def __starting_point():
    main()
__starting_point()
