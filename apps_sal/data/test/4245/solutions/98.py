A, B = map(int, input().split())
 
# 答えは、ceil((B-1)/(A-1))
A -= 1
B -= 1
print(-(-B//A))
