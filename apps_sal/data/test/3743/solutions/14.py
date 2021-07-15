# #n14 = 951069502319
# n = int(input())

# def isprime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# FOUND = -1

# x = int(n**0.5)
# if x*x == n:
#     n = x

# if not isprime(n):
#     for i in range(2, int(n**0.5)+1):
#         if isprime(i) and n%i==0:    
#             FOUND = i
#             break
#     # print (FOUND)
#     if FOUND != -1:
#         while(n % FOUND == 0):
#             n /= FOUND
#         if n == 1:
#             print (FOUND)
#         else:
#             print (1)
# else:
#     print (n)

n = int(input())

check = 0

for i in range(2,int(n**0.5)+1):
    if n%i==0:
        #khong phai snt
        check = 1
        while n%i==0:
            n /= i
        if n == 1:
            print (i)
            break
        else:
            print(1)
            break

if check == 0:
    print (n)

