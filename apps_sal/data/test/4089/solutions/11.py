import string
abc = list(string.ascii_lowercase)

n = int(input())
list1 = []

if n <= 26:
  print((abc[n-1]))
  return
  
while n > 26:
  d = n//26
  r = n % 26
  if r == 0:
    d -= 1
    r = 26
  list1.append(abc[r-1])
  n = d


list2 = (list1 + [abc[d-1]])

list2.reverse()
print((''.join(list2)))

