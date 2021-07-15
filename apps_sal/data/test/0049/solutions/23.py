#import sys
#digit = int(sys.argv[1])
digit = int(input())

if int(digit) <= 9:
    print(digit)
    return

start_range = 1
end_range = 9

power = 1
digit_count = 2
while not (start_range <= digit and digit <= end_range):
    start_range = end_range + 1
    end_range = 9 * 10**power * digit_count + start_range - 1
    power += 1
    digit_count += 1

offset_number = (digit - start_range) // (digit_count - 1)
#print(f"{digit} - {start_range} mod {digit_count-1} = {offset_number}")
number = str(10**(power - 1) + offset_number)
#print(f"10^ {power - 1} + {offset_number} = {number}")
offset_digit = (digit - start_range) % (digit_count - 1) 
#print(f"{digit} - {start_range} mod {digit_count - 1 } = {offset_digit}")
#print(f"{number} {number[-offset_digit]}")
print(f"{number[offset_digit]}")

