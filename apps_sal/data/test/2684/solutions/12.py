# cook your dish here
int(input())
test_str = input() 
#Find all unique substrings in a given string
res = set([test_str[i: j] for i in range(len(test_str)) 
          for j in range(i + 1, len(test_str) + 1)])

for val in sorted(res,key = len,reverse=True):
    if val == val [::-1]:
        print(len(val))
        print(val)
        break

