def is_arithmatic(seq):
    return all([seq[i] - seq[i-1] == seq[i-1] - seq[i-2] for i in range(2, len(seq))])

def is_geometric(seq):
    return all([seq[i] / seq[i-1] == seq[i-1] / seq[i-2] for i in range(2, len(seq))])

  
    


def main():
    numbers = input()
    numbers = numbers.split()
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
           
    if is_arithmatic(numbers):
        print(numbers[len(numbers) - 1] + (numbers[len(numbers) - 1] - numbers[len(numbers) - 2]))
        
    elif is_geometric(numbers):
              next_number = numbers[len(numbers) - 1] * ( numbers[len(numbers) - 1] / numbers[len(numbers) - 2])
              if next_number == int(next_number):
                  print(int(next_number))
              else:
                  print(42)
    else:
        print(42)
 
    

#import doctest
#doctest.testmod()
main()   

