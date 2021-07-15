h,w=map(int, input().split())

print("#"*(w+2))
for i in range(h):
    print("#{}#".format(input()))
print("#"*(w+2))
