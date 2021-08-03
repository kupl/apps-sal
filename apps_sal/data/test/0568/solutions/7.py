#import sys
#sys.stdin = open("python/in", "r")

#n, m = [int(i) for i in input().split(" ")]
n = int(input())
print(((27 ** n) - (7**n)) % 1000000007)
