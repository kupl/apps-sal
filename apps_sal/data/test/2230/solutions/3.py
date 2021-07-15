def get_candies(n):
    result = []
    bags = list(range(1, n**2 +1))

    for i in range(n):
        each = []
        for times in range(int(n / 2)):
            each.append(bags[0])
            each.append(bags[-1])
            bags = bags[1:len(bags)-1]
        each.sort()
        result.append(each)

    return result


def main():
    n = int(input())
    


    result = get_candies(n)
    
    for i in range(len(result)):
        string = ""
        for value in result[i]:
            string += str(value)
            string += " "
        print(string)
        
        
    

#import doctest
#doctest.testmod()
main()   

