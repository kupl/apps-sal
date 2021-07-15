import sys

input = sys.stdin.readline

a,b,x= map(int, input().split())

a_count = (a-1) // x


b_count = b // x
print(b_count - a_count)
