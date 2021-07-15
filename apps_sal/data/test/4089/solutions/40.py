N = int(input())
ans_reverse = ""

def num_to_alphabet(n):
  return chr(ord("a") + n)

while N:
  N -= 1
  ans_reverse += num_to_alphabet(N % 26)
  N //= 26
  
print((ans_reverse[::-1]))

