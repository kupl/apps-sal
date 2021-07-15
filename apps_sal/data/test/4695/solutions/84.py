G = [set([1,3,5,7,8,10,12]), set([4,6,9,11]), set([2])]
def check(x, y):
  for g in G:
    if x in g and y in g:
      return True
  return False
x, y = list(map(int, input().split()))
print(("Yes" if check(x, y) else "No"))

