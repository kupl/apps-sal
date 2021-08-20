class Solution:

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if len(IP) < 4:
            return 'Neither'
        if len(IP.split('.')) == 4:
            for i in IP.split('.'):
                if len(i) == 0:
                    return 'Neither'
                elif not i.isdigit():
                    return 'Neither'
                elif not 0 <= int(i) <= 255:
                    return 'Neither'
                elif (i[0] == '0') & (len(i) > 1):
                    return 'Neither'
            return 'IPv4'
        elif (len(IP.split(':')) == 8) & (IP[0] != '0'):
            hex = set('0123456789abcdefABCDEF')
            for i in IP.split(':'):
                if len(i) == 0 or len(i) > 4:
                    return 'Neither'
                elif any([j not in hex for j in i]):
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
