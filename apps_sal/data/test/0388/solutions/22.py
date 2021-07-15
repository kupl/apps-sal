import random

def random_str(rango, pos):
    while True:
        x = random.randint(65,90)
        string = chr(x)
        x = random.randint(1,10)
        for i in range(x - 1):
            rand = random.randint(97,122)
            string += chr(rand)
        if string not in rango:
            break
    return string

def print_array(array):   
    result = ""
    for string in array:
        result += string + " "

    print(result)
    
n, k = map(int, input().strip().split(" "))

strings = input().strip().split(" ")
soldiers = [-1] * n

for i in range(n):
    soldiers[i] = random_str(soldiers, i)

pos = 0
for string in strings:
    
    if string == "NO":        
        aux = soldiers[pos]
        soldiers[pos + k - 1] = aux  
              
    pos += 1
        
print_array(soldiers)    
