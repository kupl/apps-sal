# solution
import io
data = input()
g = data.count('g')
p = data.count('p')
result = (-p + (g + p) // 2)
print(result)
