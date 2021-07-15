import math
 
 
class Read:
    @staticmethod
    def string():
        return input()
 
    @staticmethod
    def int():
        return int(input())
 
    @staticmethod
    def list(sep=' '):
        return input().split(sep)
 
    @staticmethod
    def list_int(sep=' '):
        return list(map(int, input().split(sep)))
 
result = math.inf
 
def solve():
  n = Read.int()
  a = Read.list_int();
  t = 0
  for i in a:
    if i % 2 == 0:
      t += 1
  print('YES' if t == 0 or t == n else 'NO')
 
# query_count = 1
query_count = Read.int()
while query_count:
    query_count -= 1
    solve()
