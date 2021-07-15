import sys

line = input().split(" ");

test_cases = int(line[0]);

for tc in range(test_cases):
    line = input().split(" ");
    num1 = int(line[0]);
    num2 = int(line[1]);
    count = 0;
    while(num1 != 0 and num2 != 0):
        if(num1 > num2):
            count += int(num1/num2);
            num1 %= num2;
        else:
            count += int(num2/num1);
            num2 %= num1;
    
    sys.stdout.write(str(count));
    if(tc < test_cases-1):
        sys.stdout.write("\n");
