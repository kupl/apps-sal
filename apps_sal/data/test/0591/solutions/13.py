'''
Created on May 4, 2016
@author: Md. Rezwanul Haque
'''
import sys
from audioop import reverse
sys.stdin = open("input.txt", "r");
sys.stdout = open("output.txt", "w");

n, k = map(int, input().split())
p = [(x, i)for i, x in enumerate(list(map(int, input().split())), 1)]
# print(p)
p.sort(reverse=True)
# print(p)
print(p[k - 1][0])
print(" ".join(str(x[1])for x in p[:k]))
