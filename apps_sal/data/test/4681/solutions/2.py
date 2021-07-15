n = int(input())
lucas = [2,1]
for i in range(2,n+1):
    lucas.append(lucas[-2]+lucas[-1])
print(lucas[-1])
