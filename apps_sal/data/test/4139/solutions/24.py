k = int(input())

def the_algorithm(k, n, bit, count):
    if n > k: return count
    if bit == 0b111: count += 1
    
    count = the_algorithm(k, n * 10 + 7, bit | 0b001, count)
    count = the_algorithm(k, n * 10 + 5, bit | 0b010, count)
    count = the_algorithm(k, n * 10 + 3, bit | 0b100, count)
    
    return count

print((the_algorithm(k, 0, 0, 0)))

