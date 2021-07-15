import sys
import math

n = int(sys.stdin.readline())

in_str = [int(x) for x in (sys.stdin.readline()).split()]

in_str.sort(reverse=True)

result = int(math.fsum(in_str))
k = result

mv = len(in_str) - 1

while(mv > 0):
    result += in_str[mv]
    k = int(k - in_str[mv])
    result += k
    mv -= 1
    
print (result)
