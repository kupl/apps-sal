# -*- coding: utf-8 -*-
import sys


def main():
    N = int( sys.stdin.readline() )


    def gcd(a,b):
        if b == 0: 
            return a
        return gcd(b, a % b)
    

    num_cnt_dic = {}
    num_gcd = [ [0]*(N+1) for _ in range(N+1) ]

    for i in range(1, N+1):
        for j in range(1, N+1):
            g = gcd(i, j)

            num_cnt_dic[g] = num_cnt_dic.get(g, 0) + 1
            num_gcd[i][j] = g
    

    ans = 0

    for i in list(num_cnt_dic.keys()):
        for j in range(1, N+1):
            ans += (num_gcd[i][j] * num_cnt_dic[i])
    
    
    print(ans)


def __starting_point():
    main()

__starting_point()
