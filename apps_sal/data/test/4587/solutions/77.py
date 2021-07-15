def bin_src_l(arr, key):
  l = 0
  r = len(arr) - 1
  while l <= r:
    mid = (l + r) // 2
    if arr[mid] > key:
      r = mid - 1
    else:
      l = mid + 1
  
  if l < len(arr):
    return l
  else:
    return None

def bin_src_s(arr, key):
  l = 0
  r = len(arr) - 1
  while l <= r:
    mid = (l + r) // 2
    if arr[mid] >= key:
      r = mid - 1
    else:
      l = mid + 1
  
  if r >= 0 :
    return r
  else:
    return None


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A)
C = sorted(C)

sum = 0
for b in B:
  a = bin_src_s(A, b)
  c = bin_src_l(C, b)
  a = a + 1 if a is not None else None
  c = N - c if c is not None else None
  if a is not None and c is not None:
    sum += a * c
  
print(sum)
