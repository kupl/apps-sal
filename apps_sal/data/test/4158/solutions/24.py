def read_numbers():
  return (int(s) for s in input().strip().split(' '))

# keys_set = {128, 1, 2, 256, 4, 512, 1024, 2048, 8, 4096, 32768, 131072, 524288, 262144, 8192, 1048576, 16, 16384, 4194304, 32, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 64, 65536, 2097152}
# keys = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
keys = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]

def main():
  _ = input()
  dots = set(read_numbers())
  # print(keys)
  # print(dots)

  max_res = []

  for dot in dots:
    for dist in keys:
      res = [dot]
      d1 = dot - dist
      d2 = dot + dist
      if d1 in dots:
        res.append(d1)
      if d2 in dots:
        res.append(d2)
      
      if len(res) > len(max_res):
        max_res = res
      
      if len(max_res) == 3:
        print(len(max_res))
        print(' '.join(str(n) for n in max_res))
        return

  print(len(max_res))
  print(' '.join(str(n) for n in max_res))
  


def __starting_point():
  main()
__starting_point()
