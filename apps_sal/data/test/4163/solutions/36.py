# -*- coding: utf-8 -*-

n = int(input())

d_1_1, d_1_2 = map(int, input().split())
d_2_1, d_2_2 = map(int, input().split())

for _ in range(n-2):
    d_3_1, d_3_2 = map(int, input().split())
    if(d_1_1 == d_1_2 and d_2_1 == d_2_2 and d_3_1 == d_3_2):
        print('Yes')
        return
    d_1_1, d_1_2 = d_2_1, d_2_2
    d_2_1, d_2_2 = d_3_1, d_3_2
print('No')
