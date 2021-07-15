n, k = map(int, input().split())
# while making the string, k = (n - 2 * length + 2)
length = (n - k + 2) // 2           # length of a cycle
string = "0" * (length - 1) + "1"   # make the cycle
answer = string * (n // length + 1) # make the string with length >= n
print(answer[ : n])
