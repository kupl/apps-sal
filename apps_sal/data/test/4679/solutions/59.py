A = list(input())
B = list(input())
C = list(input())
li = [A, B, C]
sw = True
k = 0
while sw == True:
    if li[k][0] == 'a':
        del li[k][0]
        k = 0
    elif li[k][0] == 'b':
        del li[k][0]
        k = 1
    elif li[k][0] == 'c':
        del li[k][0]
        k = 2
    if li[k] == []:
        sw = False
ans = ['A', 'B', 'C']
print(ans[k])
