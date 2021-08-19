import io
import math
import scipy.sparse
(nim, mike, kite) = map(int, input().split())
array = list(map(int, input().split()))
print(max(abs(kite - array[nim - 1]), abs(array[nim - 1] - array[nim - 2])))
